# relay-bridge

### Example Setup

1. Create an empty folder for setting up your bridge. In this example we call it `sokol-kovan-bridge`.
`mkdir app && cd app`  

2. Start two blockchain and prepare temporary ETH address(es) for deployment by creating new account(s) in MetaMask. This account is used:
    * for deploying bridge contracts to both networks
    * as the bridge contracts management wallet
    * as the validator's wallet address(es)

3. Deploy the small contract for home chain coin and foreign chain coin. 
    * Fund Home account(s) using the  
    * Get free Kovan Coins from the [gitter channel](https://gitter.im/kovan-testnet/faucet) or [Iracus faucet](https://github.com/kovan-testnet/faucet) for Foreign account(s). Get 5 Keth to 1 acc, and transfer from there to all other wallets if more than one account is used.

4. Deploy the Sokol <-> Kovan Bridge contracts.
    * Go to the the `sokol-kovan-bridge` folder created in step 1 and `git clone https://github.com/poanetwork/poa-bridge-contracts`
    * Follow instructions in the [POA Bridge contracts repo](https://github.com/poanetwork/poa-bridge-contracts).
    * Set the parameters in the .env file.
      * `DEPLOYMENT_ACCOUNT_PRIVATE_KEY`: Export the private key from step 2
      * `HOME_RPC_URL`=https://sokol.poa.network
      * Wallet address(es) for bridge contracts management. For testing, you can use the same address for all address values in the file. This includes:
        * `HOME_OWNER_MULTISIG`
        * `HOME_UPGRADEABLE_ADMIN_VALIDATORS`
        * `HOME_UPGRADEABLE_ADMIN_BRIDGE`
        * `FOREIGN_OWNER_MULTISIG`
        * `FOREIGN_UPGRADEABLE_ADMIN_VALIDATORS`
        * `FOREIGN_UPGRADEABLE_ADMIN_BRIDGE`
        * `VALIDATORS` _Note: Wallet address(es) for validator(s) are separated by a space. For testing, you can use the same address that was used as the bridge contracts management account._
      * `FOREIGN_RPC_URL`=https://kovan.infura.io/mew
    * When deployment is finished, check that the `bridgeDeploymentResults.json` file exists in the `poa-bridge-contracts/deploy` directory and includes the bridge contract addresses.  

5. Install and run the POA Token Bridge.
    * Got to the `app` folder and `git clone https://github.com/poanetwork/token-bridge`
    * Follow instructions in the [POA Token Bridge repo](https://github.com/poanetwork/token-bridge).

If successful, you will see bridge processes run when you issue a command. For example, run `npm run watcher:*`
