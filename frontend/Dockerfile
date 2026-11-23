FROM nginx:alpine
RUN apk add --no-cache nodejs npm && npm install -g htmlhint
COPY index.html klient.css klient.js klient.html logowanie.css logo.png admin.css admin.html admin.js /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
RUN htmlhint /usr/share/ngninx/html/index.html
EXPOSE 80
