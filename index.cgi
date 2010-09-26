#!/usr/bin/ruby

require "logger";
require "cgi";
require "erb";


logger          = Logger.new('log/ruby_login_system.log', 5);
logger.level    = Logger::INFO;
logger.progname = __FILE__; 

logger.info{ 'start' }

html = {};
cgi  = CGI.new;

html = {
         :header      => { 'type' => 'text/html', 'charset' => 'utf8' },
         :bad_message => %q{ <font color="red">ユーザ名またはパスワードが不正です<br /></font> }
       };


ERB.new( File.read('./rhtml/index.rhtml') ).run(binding)


logger.info{ 'end' }
