// I'm a comment!
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.8;


import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";


contract autoSol {
    address payable public owner;
    uint256 public advancedPrice = 0.1 ether;
    event bought(bool isBought);
    constructor()payable{
        owner = payable(msg.sender);
    }

    function buySomething() public payable{
        //require (value == advancedPrice);
        payable(msg.sender).transfer(advancedPrice);
        emit bought(true);
    }

    function emptyVault() public {
        require(msg.sender == owner);
        uint amount = address(this).balance;
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Failed to send Ether");
    }

    function changeFee(uint256 newPrice) public{
        require(msg.sender == owner);
        advancedPrice = newPrice;
    }

    function checkVault() public view returns(uint256){
        require(msg.sender == owner);
        return advancedPrice;
    }

    function changeOwner(address newAddress)public{
        require(msg.sender == owner);
        owner = payable(newAddress);
    }

    function getFee()public view returns(uint256){
        return advancedPrice;
    }

}
