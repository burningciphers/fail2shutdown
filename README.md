# fail2shutdown

## Threat Model

There's [fail2ban](https://en.wikipedia.org/wiki/Fail2ban) for brute-force 
attacks over the network. But what if an attacker has physical access to
your computer? What if an attacker is sitting at your desk guessing
your password while you're sleeping? Or has stolen your laptop and is
guessing at his leisure?

`fail2shutdown` imagines the following conditions:
* an attacker with physical access
* the computer uses full-disk encryption
* the attacker does not know the FDE password

## Installing and Running

As root:
 
```
root@bcbox:~$ git clone https://github.com/burningciphers/fail2shutdown
```

Add to root's crontab

```
root@bcbox:~# crontab -l
# m h  dom mon dow   command
* * * * * /usr/bin/python3 /root/fail2shutdown/fail2shutdown.py
```
