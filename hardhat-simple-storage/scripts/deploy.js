// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// When running the script with `npx hardhat run <script>` you'll find the Hardhat
// Runtime Environment's members available in the global scope.
const { ethers, run, network } = require("hardhat")

async function main() {
  // Hardhat always runs the compile task when running scripts with its command
  // line interface.
  //
  // If this script is run directly using `node` you may want to call compile
  // manually to make sure everything is compiled
  // await hre.run('compile');

  // We get the contract to deploy
  const autoSolFactory = await ethers.getContractFactory("autoSol")
  console.log("Deploying contract...")
  const autoSol = await autoSolFactory.deploy()
  await autoSol.deployed()

  // We only verify on a testnet!
  if (network.config.chainId === 42 && process.env.ETHERSCAN_API_KEY) {
    // 6 blocks is sort of a guess
    await autoSol.deployTransaction.wait(6)
    await verify(autoSol.address, [])
  }
  console.log("Simple Storage deployed to:", autoSol.address)

}

const verify = async (contractAddress, args) => {
  console.log("Verifying contract...")
  try {
    await run("verify:verify", {
      address: contractAddress,
      constructorArguments: args,
    })
  } catch (e) {
    if (e.message.toLowerCase().includes("already verified")) {
      console.log("Already verified!")
    } else {
      console.log(e)
    }
  }
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error)
    process.exit(1)
  })
