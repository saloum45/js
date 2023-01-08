// this is a function that verifie is a someone can drive a car

function canDrive(age,pays){
    if (
        (age>=18 && pays=='FR') ||
        (age>=16 && pays=='US')
    ) {
        return true;
    }
    return false;
}

