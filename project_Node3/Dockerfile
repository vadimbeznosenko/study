FROM node:14-alpine
RUN apk add curl
WORKDIR /opt/app
ADD index.js .
HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=3 CMD curl -f http://localhost:3000 || exit 1
CMD ["node", "./index.js"]