var HDWalletProvider = require("truffle-hdwallet-provider-privkey");
require('dotenv').config()

module.exports = {
  networks: {
    development: {
      provider: () => new HDWalletProvider(["5eee76ef04b8248c15a4ac923fee6781c07f1d60a8b8307ab8c568016602902f"], "https://localhost:8545"),
      network_id: 5776,
      gas: 4465030,
      gasPrice: 21 },
    main: { host: "localhost", port: 8545,
    network_id: 2, gas: 4465030 }
  }
};
