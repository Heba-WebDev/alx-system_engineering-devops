# Install flask from pip3

package { 'flask' :
    groupensure   => '2.1.0',
    provider => 'pip3',
    }
