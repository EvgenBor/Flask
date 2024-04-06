from flask import Flask, jsonify, request
from flask.views import MethodView
from models import Advertisement, Session
from sqlalchemy.exc import IntegrityError

app = Flask('app')

class AdvertisementView(MethodView):
    def get(self, adv_id):
        with Session() as session:
            adv = session.get(Advertisement, adv_id)
            if adv is None:
                raise Exception()
            return jsonify({
                'id': adv.id,
                'title': adv.title,
                'description': adv.description,
                'creation_datetime': adv.creation_datetime,
                'owner': adv.owner
            })
    
    def post(self):
        json_data = request.json
        with Session() as session:
            adv = Advertisement(**json_data)
            session.add(adv)
            try:
                session.commit()
            except IntegrityError as err:
                raise err
            return jsonify({
                'id': adv.id,
                'title': adv.title,
                'description': adv.description,
                'creation_datetime': adv.creation_datetime,
                'owner': adv.owner
            })
                
    def delete(self, adv_id):
        with Session() as session:
            adv = session.get(Advertisement, adv_id)
            if adv is None:
                raise Exception()
            session.delete(adv)
            session.commit()
            return jsonify({'status': 'deleted'})
        
app.add_url_rule(
    '/advertisement/<int:adv_id>', 
    view_func=AdvertisementView.as_view('with_id'),
    methods=['GET', 'DELETE'])

app.add_url_rule(
    '/advertisement',
    view_func=AdvertisementView.as_view('create_advertisement'),
    methods=['POST'])

app.run()