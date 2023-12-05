# Todos
- Needs productionization:
    - select a name for the tool, and purchase a domain the app can be deployed to
    - if the js can be solely used front end, then use that (currently the js is bonked for larger bytecode)
    - otherwise containerization is likely a good idea
- The libraries used were selected without much thought. These should be reconsidered
- Consider inporting the cli file using a gitsubmodule or similar to ensure this app stays up to date with the dafny repo
- expose more of the underlying functionality of the cli to the end user
- some sort of load balancing in production (should be easy since it is stateless)
- some sort of DOS protection/santization of the input
- FAQ section with links to explain why we created the tool
- better error handling
- currently the cli tool is called and its dot file output collected via stdout. this has a hardcoded limit 
- CI/CD
- testing
    - standard front end unit tests
- monitoring
    - checkly or similar service that runs periodically, enters an input and checks some type of cfg is generated


Feature ideas:
- ability to input a contract address (vs. bytecode) and the bytecode will automatically be retrieved. tenderly does a nice network agnostic version of this. 
- the ability to toggle on/off tool tips

Potential resources required:
- Front end engineer
- Designer




This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
