description=[[Get HTTP server info]]
portrule=function(host,port)
return port.number==80 or port.number==8080
end
action=function(host.port)
return "HTTP Server running on port" .. port.number
end

