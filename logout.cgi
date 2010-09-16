#!/usr/bin/ruby

require "cgi"
require 'cgi/session'


cgi      = CGI::new
session  = CGI::Session.new(cgi, 'session_expires' => Time.now - 1)
session.delete

print cgi.header({ 'status' => 'REDIRECT', 'Location' => 'index.cgi' })

