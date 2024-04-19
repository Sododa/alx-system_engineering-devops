# 1-install_a_package.pp

# Ensure the 'python3-pip' package is installed
package { 'python3-pip':
  ensure => installed,
}

# Use pip3 to install Flask version 2.1.0
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  # Check if Flask 2.1.0 is already installed
  unless  => '/usr/bin/pip3 show Flask | grep -q "^Version: 2.1.0$"',
  require => Package['python3-pip'], # Ensure python3-pip is installed first
  path    => '/usr/local/bin:/usr/bin', # Add appropriate path for pip3
}

# Notify the user about the installation
notify { 'Flask installed successfully':
  subscribe => Exec['install_flask'],
}
