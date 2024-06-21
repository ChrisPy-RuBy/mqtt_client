import paho.mqtt.publish as publish

publish.single("paho/test/topic", "payload", hostname="mqtt.eclipseprojects.io")
