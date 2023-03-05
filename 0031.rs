fn main() {
    let mut count = 0;
    for a in 0..=200 {
        for b in 0..=100 {
            for c in 0..=40 {
                for d in 0..=20 {
                    for e in 0..=10 {
                        for f in 0..=4 {
                            for g in 0..=2 {
                                for h in 0..=1 {
                                    let sum = a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h;
                                    if sum == 200 {
                                        count += 1;
                                    }
    }}}}}}}}
    println!("{}", count);
}
