import json
env_vars = {}
with open("../../token-bridge/.env.example") as f:
    for line in f:
        if line.startswith('#') or not line:
            continue
        try:
          key, value = line.strip().split('=', 1)
        except:
          print(line)
        env_vars[key]=  value # Save to a list




with open("bridgeDeploymentResults.json", "r") as content:
  config = json.load(content)
  env_vars['ERC20_TOKEN_ADDRESS']=config['homeBridge']['erc677']['address']
  env_vars['FOREIGN_BRIDGE_ADDRESS']=config['foreignBridge']['address']
  env_vars['HOME_BRIDGE_ADDRESS']=config['homeBridge']['address']
  env_vars['HOME_START_BLOCK']=config['homeBridge']['deployedBlockNumber']
  env_vars['HOME_FOREIGN_BLOCK']=config['foreignBridge']['deployedBlockNumber']
  print(env_vars)

with open('../../token-bridge/.env','w')  as f:
  for i in env_vars.iteritems():
    print(i)
    f.write("%s=%s\n" %i)
