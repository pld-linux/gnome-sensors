dnl
dnl see if MonitorSensors is installed
dnl

AC_DEFUN(AC_CHECK_MONITORSENSORS,[
	AC_CHECK_PROG(found_monitorsensors,"MonitorSensors","yes", "no")
	if test "$found_monitorsensors" = "yes"; then
		AC_DEFINE(HAS_MONITORSENSORS)
		echo "***";
		echo "*** MonitorSensors was located on your machine";
		echo "*** A menu item will be added to GnomeSensors.";
		echo "***";
	fi
])

dnl
dnl test for the presense of the lm_sensors module and library
dnl
AC_DEFUN(AC_CHECK_SENSORS,[
	AC_SUBST(SENSORS_LIBS)
	AC_SUBST(SENSORS_INCLUDEDIR)
	has_sensors=false
	search_sensors=true	
	AC_SEARCH_SENSORS()
	if test $has_sensors = false; then
		echo "***";
		echo "***";
		echo "*** lm_sensors was not located on your machine.";
                echo "*** GnomeSensors will not compile."
		echo "***";
		echo "*** Please install lm_sensors and try again.";
		echo "***";
		echo "***";
		exit;
	fi
])

dnl
dnl 
dnl
AC_DEFUN(AC_SENSORS, [
    if $search_sensors
    then
        if test -f $1/$2
	then
	    AC_MSG_RESULT(Found sensors on $1/$2)
 	    SENSORS_LIBS="$3"
	    SENSORS_INCLUDEDIR="$4"
	    search_sensors=false
	    screen_manager=$5
            AC_DEFINE(HAS_SENSORS)
            has_sensors=true
	    echo "***";
            echo "*** lm_sensors was located on your machine.";
            echo "*** you will be able to compile GnomeSensors";
            echo "***";
	fi
    fi
])

AC_DEFUN(AC_SEARCH_SENSORS, [
    AC_CHECKING("location of sensors.h file")

    AC_SENSORS(/usr/include, sensors.h, -lsensors,, "sensors localated in /usr/include")
    AC_SENSORS(/usr/include/sensors, sensors.h, -lsensors, -I/usr/include/sensors, "sensors located in /usr/include/sensors")
    AC_SENSORS(/usr/local/include, sensors.h, -L/usr/local/lib -lsensors, -I/usr/local/include, "sensors located in /usr/local/include")
    AC_SENSORS(/usr/local/include/sensors, sensors.h, -L/usr/local/lib -L/usr/local/lib/sensors -lsensors, -I/usr/local/include/sensors, "sensors located in /usr/local/include/sensors")
])




 
