import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("paho/test/topic", hostname="mqtt.eclipseprojects.io")
print("%s %s" % (msg.topic, msg.payload))
