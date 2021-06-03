# SAW: System Automated Watchdog for Windows.

Designed with PAGE but I modified many parts of the generated GUI code to exactly meet my needs. 
Using python 3.8.5 and tkinter. I used While loop with tkinter which should cause GUI freeze but I bypassed this inconvenience and I broke the limits!

Successfully tested on Windows 10 pro and Windows Server 2016/2019.

Computer Resource Monitoring which display pop-up notification and automated alerting email is sent if conditions are not met.

To successfully compile code with pyinstaller: 

- First install needed librairies with  `pip install -r requirements.txt`
- Add icon_path for show_toast notification.
- Compile the code using pyinstaller by running this command:   `pyinstaller --onefile SAW.py` or install the software via the provided setup.


![System WATCHDOG.gif](https://github.com/IT-Support-L2/System-WATCHDOG/blob/main/SWD.gif)

  
# All inputs are mandatory!

# System Preferences Inputs

# •	CPU 

# What is CPU?

Central Processing Unit or CPU is a small but mighty computer chip found on top of the motherboard in your PC. It’s placed into the CPU socket with its pins facing down. A small lever keeps it secure.
CPUs generate a lot of heat, even when running for a short amount of time. Due to this thermal activity, the CPU is usually attached to a heat sink with a fan located right on top of it. In most cases, these two components will arrive bundled if you buy a CPU.
In Windows, CPU is monitored using percentage unit measurement.

# What should I input in CPU tab?

Simply input the CPU usage percentage allowed so if the software detects higher percentage than input, you will be notified by a screen pop-up and an email alert will be automatically sent. As an example, let’s say you do not allow more than 50% CPU usage, simply in CPU tab input 50.

# •	RAM
# What is RAM?

Random-access memory or RAM is a form of computer memory that can be read and changed in any order, typically used to store working data and machine code. A random-access memory device allows data items to be read or written in almost the same amount of time irrespective of the physical location of data inside the memory.

# What should I input in RAM tab?

Let’s say your computer or server has 32GB RAM and in normal state, it does not consume more than 20GB as an example so if it’s consuming more, it means something wrong. To receive an alert of RAM exceeding 20GB, simply input 20. 


# •	Storage

# What is storage?

Computer data storage is a technology consisting of computer components and recording media that are used to retain digital data. It is a core function and fundamental component of computers. The central processing unit (CPU) of a computer is what manipulates data by performing computations. 
In Windows, storage is monitored using percentage unit measurement.

# What should I input in Storage tab?

Sure, you don’t want your server or computer exceed 80% of its storage without getting notified, so simply input 80, as an example.

# •	Ping / Reachability Check

# What is Ping or IP Reachability?	

Ping is a computer network utility used to test the reachability of a host (which could be server, computer, smartphone, surveillance cam, basically any online device) on an Internet Protocol network. 

# What should I input in Ping / Reachability Check?

Enter the IP address of the host you need to check its reachability in loop.
As an example: 8.8.8.8 which is Google Public DNS.

# •	Upload Speed Check

# What is Upload Speed?

Upload speed is the number of bytes per second you can send. For a normal ADSL subscription, usually the upload speed is around 1.5 Mbps.

# What should I input in Upload Speed Check tab?

For example, let’s say you want to get notified as Upload Speed drops under 
1 Mbps, simply input 1.

# •	Download Speed Check

# What is Download Speed?
Download speed is the rate your connection receives data.

# What should I input in Download Speed Check tab?

If you have for example 20 Mbps Download Speed and you need to be notified as it drops under 15 Mbps, then input 15.

# •	Latency Check

# What is Latency?

Network latency is the term used to indicate any kind of delay that happens in data communication over a network. In other words, it is the time that for example an email needs to travel to its final destination. The best latency rate is around 35 MS and the worst is 100 MS or more. (MS means milliseconds)

# What should I input in Latency Check?

As explained, if latency goes over 100 MS, your internet will be very slow and most of your requests will be answered by Request Timed Out which will have crucial impact on your servers performance.

As an example, to receive instant alert for latency over 35 MS, input 35.

# •	Timer

# What is Timer?

It is the time interval in seconds in which all checks will be executed in  infinite loop unless you click on Stop. I recommend to set it to 60 which equals to 60 seconds.

# What should I input?

Let’s say, you need to execute all checks every 10 seconds. Simply input 10.


# Email Preferences 


# •	SMTP

# What is SMTP?

SMTP or The Simple Mail Transfer Protocol is a communication protocol for electronic mail transmission.

# What should I input in SMTP tab?

If you are using Outlook than your SMTP is smtp-mail.outlook.com, for Gmail it’s smtp.gmail.com, else ask your email service provider to acquire its SMTP server address.

# •	Sender Email Address

Input your email address

# •	Sender’s Password

Input your password.

Important Note: You will not receive automated emails alerts if you are using 2-factor authentication.

Best Suggestion: I suggest to register new email address for this purpose only.

# •	Receiver Email Address

Input the receiver’s email address. 
Hint: It could be the sender’s email address as well.

# •	Start

# What does Start button do?

Once you click on Start, System Automated Watchdog will start monitoring your computer resources and watch over your computer or server. It will start by running first check than after each time interval (seconds), If one or more condition(s) are not met, you will get screen pop-up notification and an automated email will be sent to the receiver using sender’s smtp server address, email address and password.

If an exception or error occured, the software will stop running with an error message. Fix your inputs and run it again.

# •	What does Stop button do?

If you need to update your inputs or you don’t want to keep the software running, simply click on Stop.

# • Why after clicking on Start, the software start instantly monitoring while the time interval is set to 60 seconds?

SAW or System Automated Watchdog will instantly run a first and only 1 thread regardless of the time interval you set.

# •	Why after clicking on Stop, I still getting po-up notifications and alerting emails?

When you click on Stop, SAW will be stopped after finishing the running threads or the running tasks, so it’s a very normal behavior. 



Cheers 🙂







