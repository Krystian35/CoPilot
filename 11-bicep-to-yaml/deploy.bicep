// Load default configuration values
var var_default = loadYamlContent('deploy.yaml', 'default')
var var_virtualNetwork = loadYamlContent('deploy.yaml', 'virtualNetwork')
var var_networkSecurityGroup = loadYamlContent('deploy.yaml', 'networkSecurityGroup')

// Deploy Network Security Group for monitoring services
module module_networkSecurityGroup 'br/public:avm/res/network/network-security-group:0.5.1' = {
  name: 'deploy-${var_networkSecurityGroup.name}'
  params: {
    name: var_networkSecurityGroup.name

    location: var_default.location
    lock: var_networkSecurityGroup.lock
    tags: var_networkSecurityGroup.tags
  }
}

// Deploy Virtual Networks for monitoring services
module module_virtualNetwork 'br/public:avm/res/network/virtual-network:0.7.1' = [
  for vnet in var_virtualNetwork: {
    name: 'vnet-${vnet.name}'
    params: {
      name: vnet.name
      addressPrefixes: vnet.addressPrefixes
      subnets: [
        for sn in vnet.subnets: {
          name: sn.name
          addressPrefix: sn.addressPrefix

          networkSecurityGroupResourceId: empty(sn.nsgName) ? null : resourceId(
            'Microsoft.Network/networkSecurityGroups',
            sn.nsgName
          )

          privateEndpointNetworkPolicies: sn.?privateEndpointNetworkPolicies ?? null
          privateLinkServiceNetworkPolicies: sn.?privateLinkServiceNetworkPolicies ?? null

        }
      ]

      location: var_default.location
      lock: vnet.lock
      tags: vnet.tags
    }
  }
]

output out_networkSecurityGroupName string = module_networkSecurityGroup.outputs.name
output out_networkSecurityGroupResourceId string = module_networkSecurityGroup.outputs.resourceId
