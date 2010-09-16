#!/usr/bin/ruby

require "cgi";

html = {};
cgi  = CGI.new;

html = {
         :header => { 'type' => 'text/html', 'charset' => 'utf8' },

         :head   => %q{
                      <html>
                      <head><titel>ログイン</title></head>
                      <body>
                    },

         :body   => %q{
                      <form action="login.cgi" method="post">
                      <table width="300" border="0" cellspacing="0" cellpadding="2">
                        <tr><td>ユーザ名:</td><td><input type="text" name="user" /></td></tr>
                        <tr><td>パスワード：</td><td><input type="password" name="password" /></td></tr>
                        <tr><td colspan="2"><center><input type="submit" value="ログイン" /></center></td></tr>
                      </table>
                      </form>
                    },
               

         :foot   => %q{
                      </body>
                      </html>
                    }, 

         :bad_message => %q{ <font color="red">ユーザ名またはパスワードが不正です<br /></font> }
       };


if( cgi['bad'] == 1.to_s ) then
  cgi.out(html[:header]){ html.values_at(:head, :bad_message, :body, :foot).join("\n") }
else
  cgi.out(html[:header]){ html.values_at(:head, :body, :foot).join("\n") }
end
