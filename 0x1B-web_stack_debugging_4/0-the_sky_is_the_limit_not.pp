# Increase traffic Nginx server can take.
exec { 'fix-nginx-traffic':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart server.
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'

}
