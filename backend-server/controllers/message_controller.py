from flask import jsonify, request
from datetime import datetime
from models.message_model import Message
from models.user_model import User


def add_message():
    try:
      from_user_id = request.json.get('from')
      to_user_id = request.json.get('to')
      message_text = request.json.get('message')

      if not from_user_id or not to_user_id or not message_text:
        return jsonify({"msg": "Missing required fields"}), 400

      sender = User.objects.get(id=from_user_id)
      if not sender:
          return jsonify({"msg": f"Sender with id {from_user_id} not found"}), 404
      
      recipients = [from_user_id, to_user_id]

      message = Message(
          text=message_text,
          users=recipients,
          sender=sender,
          timestamp=datetime.utcnow()
      )
      message.save()

      return jsonify({"msg": "Message added successfully."}), 200
    
    except Exception as ex:
        return jsonify({"msg": str(ex)}), 500

def get_messages():
    try:
        from_user_id = request.json.get('from')
        to_user_id = request.json.get('to')

        if not from_user_id or not to_user_id:
          return jsonify({"msg": "Missing required fields"}), 400
        
        messages = Message.objects(users__all=[from_user_id, to_user_id]).order_by('timestamp')

        projected_messages = []
        for msg in messages:
            from_self = str(msg.sender.id) == from_user_id
            projected_messages.append({
                "fromSelf": from_self,
                "message": msg.text
            })

        return jsonify(projected_messages), 200

    except Exception as ex:
        return jsonify({"msg": str(ex)}), 500
