pragma solidity >= 0.8.11 <= 0.8.11;
//carpool solidity code
contract Organ {
    string public users;
    string public donor_history;
    string public patient_history;
       
    //add user details to Blockchain memory	
    function addUser(string memory us) public {
       users = us;	
    }
   //get user details
    function getUser() public view returns (string memory) {
        return users;
    }

    //add donor history to Blockchain memory
    function setDonor(string memory d) public {
       donor_history = d;	
    }

    function getDonor() public view returns (string memory) {
        return donor_history;
    }

    //add patient history to Blockchain memory
    function setPatient(string memory p) public {
       patient_history = p;	
    }

    function getPatient() public view returns (string memory) {
        return patient_history;
    }

    constructor() public {
        users = "";
	patient_history ="";
	donor_history = "";
    }
}