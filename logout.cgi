#!/usr/bin/ruby

require "logger"
require "cgi"
require 'cgi/session'

logger          = Logger.new('log/ruby_login_system.log', 5);
logger.level    = Logger::INFO;
logger.progname = __FILE__;

logger.info{ 'satart' }

cgi      = CGI::new
session  = CGI::Session.new(cgi, 'session_expires' => Time.now - 1)
session.delete

print cgi.header({ 'status' => 'REDIRECT', 'Location' => 'index.cgi' })

logger.info{ 'end' }
