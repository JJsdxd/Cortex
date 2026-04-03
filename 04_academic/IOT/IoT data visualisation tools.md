#Academic/S2/IOT
Tools used to graphically display data for providing **a better overall understanding**
Reduces the complexity of raw data 

Aids in quick monitoring and analysis 
	Real-Time Monitoring
		Track sensor readings, device status, or events live.
	Trend Analysis
		Understand patterns over time, e.g., temperature variations, energy usage.
	Anomaly Detection
		Identify unusual behavior or faults in devices or systems.
	Decision Support
		Support predictive maintenance, resource allocation, or operational decisions.
	Communication
		Present IoT data to non-technical stakeholders via dashboards.
Layered Architecture
![[Data Analytics Architecture]]

Device Layer(Data Collection)
	Sensors/Actuators 
	continuous generation of data 
	usually has a micro-controller like raspberry pi/esp32 
Gateway Layer(Data Transmission)
	Means of sending data to cloud/edge processing systems
	IoT Gateways
	protocols include 
		[[LoRaWAN]]
		[[MQTT]]
		[[COAP]]
		[[HTTP]]
		[[WiFi]]
Data Storage Layer(Data bases)
	Cloud platforms such as AWS IoT, Microsoft Azure IoT, Google Cloud IoT,[[Apache web servers]]
	Databases such as [[No SQL Databases Vs SQL Databases]], Data lakes,etc
Analytics and Processing Layer
	Real time Analytics
	Batch Processing 
	Machine Learning Models
	AI - driven Prediction Systems
	[[Data Analytics]]
	usually algorithms built to process the data being collected and stored to give meaningful insight via mediums such as visualization tools
	