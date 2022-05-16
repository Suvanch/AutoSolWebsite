// SPDX-License-Identifier: GPL-3.0



pragma solidity >=0.7.0 <0.9.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";


contract contractCreator {
    address payable public owner;
    uint256 public advancedPrice = 0.1 ether;

    constructor()payable{
        owner = payable(msg.sender);
    }

    function buySomething() public payable returns (bool){
        require (msg.value == advancedPrice);
        payable(msg.sender).transfer(advancedPrice);
        return true;
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

}
