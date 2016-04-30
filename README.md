# fail2shutdown

## Threat Model

There's [fail2ban](https://en.wikipedia.org/wiki/Fail2ban) for brute-force 
attacks over the network. But what if an attacker has physical access to
your computer? What if an attacker is sitting at your desk guessing
your password while you're sleeping? Or has stolen your laptop and is
guessing at his leisure? `fail2shutdown` turns off your computer after
a set number of failed login attempts.

`fail2shutdown` imagines the following conditions:
* an attacker has physical access
* the computer uses full-disk encryption
* the attacker does not know the full-disk encryption password
* the full-disk encryption password is sufficiently long and complex 

If you don't use full-disk encryption, `fail2shutdown` only slows down
an attacker with physical access.

## Installing and Running

1. As root:
    ```
    root@bcbox:~$ git clone https://github.com/burningciphers/fail2shutdown
    ```
2. Open `fail2shutdown.py` and set the values for MAX_ATTEMPTS and 
DURATIONS.

3. Add the script to root's crontab.
    ```
    root@bcbox:~# crontab -l
    # m h  dom mon dow   command
    * * * * * /usr/bin/python3 /root/fail2shutdown/fail2shutdown.py
    ```
