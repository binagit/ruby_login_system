#!/usr/bin/ruby

require "logger";
require "mysql"
require "cgi"
require 'cgi/session'

logger          = Logger.new('log/ruby_login_system.log', 5);
logger.level    = Logger::DEBUG;
#logger.level    = Logger::INFO;
logger.progname = __FILE__; 

logger.info{ 'start' }

cgi      = CGI::new
session  = CGI::Session.new(cgi)

my       = Mysql::new('localhost', 'root', '', 'db_login')
psql     = 'select * from users where name = ? and password = md5(?)'
pstmt    = my.prepare( psql )

logger.debug{ cgi['user'] + ' ' + cgi['password'] }
pstmt.execute( cgi['user'], cgi['password'] )

if( pstmt.num_rows == 1 ) then
                               logger.info{ 'welcome.cgiに遷移' }
                               session['user'] = pstmt.fetch[1]; 
                               print cgi.header({ 'status' => 'REDIRECT', 'Location' => 'welcome.cgi' })
                          else
                               logger.info{ 'index.cgi?bad=1に遷移' }
                               print cgi.header({ 'status' => 'REDIRECT', 'Location' => 'index.cgi?bad=1' })
                          end

logger.info{ 'end' }
