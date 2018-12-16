import json
env_vars = {}
with open("../../bridge-ui/.env.example") as f:
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
  env_vars['REACT_APP_FOREIGN_BRIDGE_ADDRESS']=config['foreignBridge']['address']
  env_vars['REACT_APP_HOME_BRIDGE_ADDRESS']=config['homeBridge']['address']
  env_vars['REACT_APP_HOME_HTTP_PARITY_URL']='http://localhost:8080'
  env_vars['REACT_APP_FOREIGN_HTTP_PARITY_URL']='http://localhost:8545'
  print(env_vars)

with open('../../bridge-ui/.env','w')  as f:
  for i in env_vars.iteritems():
    print(i)
    f.write("%s=%s\n" %i)
