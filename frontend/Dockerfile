FROM node:lts-alpine as build 

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

FROM nginx:stable-alpine AS deploy-static

WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=build /app/build .
ENTRYPOINT ["nginx", "-g", "daemon off;"]
