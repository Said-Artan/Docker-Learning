Docker Learning

Flask App with Load Balancing Using Docker & NGINX

This project spins up multiple instances of a simple Flask web app and load balances them using NGINX, all with Docker Compose.

Stack:
  -Python + Flask + Redis (Basic web app)
  -Docker
  -Docker Compose
  -NGINX (as a reverse proxy + load balancer)

How to run:
 -docker-compose up --build --scale web=5
You can replace 5 with any number and NGINX will spin up that number of instances of the web app. This van be accessed at http://localhost, each time you refresh NGINX will direct you to another flask container, thanks to NGINX load balancing. 




  
<img width="551" height="439" alt="Screenshot 2025-07-17 at 19 26 36" src="https://github.com/user-attachments/assets/cfa38e61-949c-46af-936a-699dd08a4c2a" />


<img width="759" height="279" alt="Screenshot 2025-07-17 at 19 25 51" src="https://github.com/user-attachments/assets/e26b9c3c-b843-41b7-9dab-c3309e88f9a0" />





