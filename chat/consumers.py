from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync
from utils.face_analysis import YUVtoRGB, process_faces


class ApiConsumer(JsonWebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'events',
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        print("Closed websocket with code: ", close_code)
        async_to_sync(self.channel_layer.group_discard)(
            'events',
            self.channel_name
        )
        self.close()

    def receive_json(self, content, **kwargs):
        print("Received event: {}".format(content))

        # rgb = YUVtoRGB(content['face'])
        # process_faces(rgb)

        self.send_json(content)

    def events_alarm(self, event):
        self.send_json(
            {
                'type': 'events.alarm',
                'content': event['content']
            }
        )