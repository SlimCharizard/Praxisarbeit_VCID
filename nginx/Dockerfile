#install nginx image 
FROM nginx

#Remove original default conf
RUN rm /etc/nginx/conf.d/default.conf

#copy own nginx conf
COPY nginx.conf /etc/nginx/conf.d/