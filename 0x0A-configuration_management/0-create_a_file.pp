# Puppet program to create file in /tmp/school directory.

file {'/tmp/school':
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}
