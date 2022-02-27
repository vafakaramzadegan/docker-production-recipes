vcl 4.0;

import std;

backend server_nginx_0 {
    .host = "web_server";
    .port = "8080";
}

sub vcl_recv {
    
}

sub vcl_backend_response {
    
}

sub vcl_deliver {
    unset resp.http.Via;
    unset resp.http.X-Varnish;
    unset resp.http.X-Powered-By;
    unset resp.http.Server;
}