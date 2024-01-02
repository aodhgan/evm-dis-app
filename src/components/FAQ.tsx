import React from 'react';

const FAQ = () => {

    return (
        <div>
            <div className="faq">

                <section className="dark:bg-gray-800 dark:text-gray-100">
                    <div className="container flex flex-col justify-center p-4 mx-auto md:p-8">
                        {/* <p className="p-2 text-sm font-medium tracki text-center uppercase">How it works</p> */}
                        <h2 className="mb-12 text-4xl font-bold leadi text-center sm:text-5xl">Frequently Asked Questions</h2>
                        <div className="grid gap-10 md:gap-8 sm:p-3 md:grid-cols-2 lg:px-12 xl:px-32">
                            <div>
                                <h3 className="font-semibold">What is Bytespector?</h3>
                                <p className="mt-1 dark:text-gray-400">Bytespector is an easy to use tool for constructing a Control Flow Graph from EVM bytecode.</p>
                            </div>
                            <div>
                                <h3 className="font-semibold">How does it work?</h3>
                                <p className="mt-1 dark:text-gray-400">Read <a href="https://www.mantle.xyz/blog/research/decompiling-evm-bytecode">here</a> for more details.</p>
                            </div>
                            <div>
                                <h3 className="font-semibold">Is it open source?</h3>
                                <p className="mt-1 dark:text-gray-400">Yes - the code base can be found <a href="https://github.com/franck44/evm-dis">here.</a></p>
                            </div>
                            <div>
                                <h3 className="font-semibold">My bytecode doesnt work or I need more help</h3>
                                <p className="mt-1 dark:text-gray-400">Create a Github issue <a href="https://github.com/franck44/evm-dis/issues">here</a> or email aodhgan@mantle.xyz</p>
                            </div>
                        </div>
                    </div>
                </section>


                {/* Add more FAQ items here */}
            </div>
        </div>
    );

};

export default FAQ;

