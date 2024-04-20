# Define SSH client configuration file path
$ssh_config_file = '/home/ubuntu/.ssh/config'

# Ensure SSH client configuration file exists
file { $ssh_config_file:
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Configure SSH client to use specific private key and disable password authentication
file_line { 'Set IdentityFile':
  path    => $ssh_config_file,
  line    => '    IdentityFile ~/.ssh/school',
  match   => '^#?\s*IdentityFile.*',
  ensure  => present,
}

file_line { 'Disable PasswordAuthentication':
  path    => $ssh_config_file,
  line    => '    PasswordAuthentication no',
  match   => '^#?\s*PasswordAuthentication.*',
  ensure  => present,
}

# Notify the changes applied
notify { 'SSH client configuration updated':
  message => 'SSH client configuration updated successfully',
}
