#!/usr/bin/ruby

require "logger"
require "cgi"
require 'cgi/session'


logger          = Logger.new('log/ruby_login_system.log', 5);
logger.level    = Logger::INFO;
logger.progname = __FILE__;

logger.info{ 'start' }

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

if( session['user'].nil? ) then
  logger.info{ %q{session['user']が空なのでindex.cgiに遷移} }
  print cgi.header({ 'status' => 'REDIRECT', 'Location' => 'index.cgi' });
else
  logger.info{ 'ユーザの画面を表示' }
  cgi.out(html[:header]){ html[:head] + 'こんにちは' + session['user'] + html[:body] + html[:foot] }
end

logger.info{ 'end' }
