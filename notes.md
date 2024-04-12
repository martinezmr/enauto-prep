Scripts\activate.bat in ENAUTO-PREP folder to activate venv

------------------------------------------------------------------------------------
APIs

Three different styles of APIs
- RPC
- SOAP
- RESTFUL

Remote Procedure Calls (RPC)
- predates SOAP and REST style of APIs
- invokes a method or procedure on the remote system
- RPC uses XML, JSON, and any other transfer format (CSV, YAML, etc.)

Simple Object Access Protocol (SOAP)
- highly structured protocol for web service access
- SOAP is a protocol (important to keep that in mind since REST is not a protocol)
- requires XML
- support discovery (WSDL) (can expose information from the remote server like asking what calls can it use)
- can be used over any underlying transport protocol (HTTP, SMTP, etc.)
- SOAP Structure
    - SOAP envelope
    - SOAP Header contains header blocks
    - SOAP Body contains message block


Synchronous Calls
- every step has to go in order
- everything is processed in the order you enter the line


Asynchronous Calls
- an efficient way to ensure your program can respond to users while doing API calls in the background
------------------------------------------------------------------------------------