FROM node:14-alpine as build
WORKDIR /opt/app
ADD . .
RUN npm i && npm run build api

FROM node:12.22.9-alpine3.15
WORKDIR /opt/app
ADD package.json ./
RUN npm i --only=prod
COPY --from=build /opt/app/dist/apps/api ./dist
CMD ["node", "./dist/main.js"]

