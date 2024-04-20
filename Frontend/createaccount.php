<?php
// Step 1: Establish Database Connection$servername = "localhost";
$username = "root";
$password = "";
$dbname = "user";  

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Step 2: Retrieve Form Data
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $aadhar = $_POST['aadhar'];
    $dob = $_POST['dob'];
    $phone_number = $_POST['phone_number'];

    // Step 3: Validate Data (Optional)

    // Step 4: Prepare SQL Statement
    $sql = "INSERT INTO your_table_name (name, aadhar, dob, phone_number)
            VALUES ('$name', '$aadhar', '$dob', '$phone_number')";

    // Step 5: Execute SQL Query
    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        // Step 6: Handle Errors
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Step 7: Close Database Connection
$conn->close();
?>
