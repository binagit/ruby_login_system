#!/usr/bin/ruby

require "mysql"
require "cgi"
require 'cgi/session'


cgi      = CGI::new
session  = CGI::Session.new(cgi)

my       = Mysql::new('localhost', 'root', '', 'db_login')
psql     = 'select * from users where name = ? and password = md5(?)'
pstmt    = my.prepare( psql )

pstmt.execute( cgi['user'], cgi['password'] )

if( pstmt.num_rows == 1 ) then session['user'] = pstmt.fetch[1]; 
                               print cgi.header({ 'status' => 'REDIRECT', 'Location' => 'welcome.cgi' })
                          else print cgi.header({ 'status' => 'REDIRECT', 'Location' => 'index.cgi?bad=1' })
                          end


