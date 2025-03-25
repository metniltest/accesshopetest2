
FROM node:18-alpine

WORKDIR /app

COPY ./ /app

RUN npm install next react react-dom

EXPOSE 3000

CMD ["npm", "run", "dev"]
