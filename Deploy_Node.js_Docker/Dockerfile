FROM node:10.16-alpine 
RUN mkdir /nodeapp
WORKDIR /nodeapp
RUN npm i npm@latest -g 
RUN npm i nodemon@latest -g 
COPY package.json package-lock.json* /nodeapp/ 
RUN npm install --no-optional && npm cache clean --force 
COPY . /nodeapp 
CMD ["nodemon", "app.js"]
