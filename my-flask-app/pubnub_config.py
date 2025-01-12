from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-19ffbb16-9bb0-425c-b050-929ba2543c0e'
pnconfig.publish_key = 'pub-c-3b8b7e3d-1c2c-4e0a-8f2c-7b8e1f6e0c9e'
pnconfig.uuid = 'iot-ica'

pubnub = PubNub(pnconfig)