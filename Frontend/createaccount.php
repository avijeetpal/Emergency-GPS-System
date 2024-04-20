<?php
// Database connection parameters
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "user";  

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve form data
$name = $_POST['name'];
$aadhar = $_POST['aadhar'];
$dob = $_POST['dob'];
$phone_number = $_POST['phone_number'];

// Prepare SQL statement to insert data
$sql = "INSERT INTO data (name, aadhar, dob, phone_number) VALUES ('$name', '$aadhar', '$dob', '$phone_number')";

// Execute SQL statement
if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close connection
$conn->close();
?>
