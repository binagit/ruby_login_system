#!/usr/bin/ruby

require "cgi"
require 'cgi/session'


html = {
         :header => { 'type' => 'text/html', 'charset' => 'utf8' },

         :head   => %q{
                      <html>
                      <head><titel>ログイン</title></head>
                      <body>
                    },

         :body   => %q{
                      <br />
                      <a href="logout.cgi">ログアウト</a>
                    },
               

         :foot   => %q{
                      </body>
                      </html>
                    }
       };



cgi      = CGI::new
session  = CGI::Session.new(cgi)

if( session['user'].nil? ) then print cgi.header({ 'status' => 'REDIRECT', 'Location' => 'index.cgi' }); exit; end

cgi.out(html[:header]){ html[:head] + 'こんにちは' + session['user'] + html[:body] + html[:foot] }
