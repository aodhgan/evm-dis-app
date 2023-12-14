# Step 1: Choose a base image with the specific Node.js version
FROM node:18.17.0

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy package.json and package-lock.json
COPY package*.json ./

# Step 4: Install dependencies
RUN npm install

# Step 5: Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Step 6: Copy your Next.js application to the container
COPY . .

# Step 7: Build your Next.js application
RUN npm run build

# Step 8: Expose the port your app runs on
EXPOSE 3000

# Step 9: Define the command to run your app
CMD ["npm", "start"]
