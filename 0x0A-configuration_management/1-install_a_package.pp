# installs flask from pip3
package { 'flask':
  command  => '2.1.0',
  provider => 'pip3'
}
