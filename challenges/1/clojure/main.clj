(defn is-divisible
  [values]
  (fn [val]
    (reduce #(or %1 %2) (map #(= (mod val %) 0) values))))

(defn divisibles
  "Generate a list of divisible values"
  []
  (filter (is-divisible [3 5]) (range 1000)))

(defn main
  "Sum all integers under 1000 that are divisible by 3 or 5"
  []
  (println (reduce + (divisibles))))

(main)
